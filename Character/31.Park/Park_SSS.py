import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0 && Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill"))
         {       
         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         MoveLocation("31.Park_Bozo", f.heroID[cp], cp, "Anywhere");
            if (cp < 3)
            {
               if (Bring(3, AtLeast, 1, f.heroID[3], "31.Park_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[3], 3, "Anywhere");
               }
               else if (Bring(4, AtLeast, 1, f.heroID[4], "31.Park_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[4], 4, "Anywhere");
               }
               else if (Bring(5, AtLeast, 1, f.heroID[5], "31.Park_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[5], 5, "Anywhere");
               }

            }
            else if (cp >= 3)
            {
               if (Bring(0, AtLeast, 1, f.heroID[0], "31.Park_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[0], 0, "Anywhere");
               }
               else if (Bring(1, AtLeast, 1, f.heroID[1], "31.Park_Bozo"))
               {
                  MoveLocation(f.location[cp],f.heroID[1], 1, "Anywhere");
               }
               else if (Bring(2, AtLeast, 1, f.heroID[2], "31.Park_Bozo"))
               {
                  MoveLocation(f.location[cp], f.heroID[2], 2, "Anywhere");
               }
            }
         MoveUnit(All, f.heroID[cp], cp, "Anywhere", f.location[cp]);
         }
         if (f.loop[cp] == 0)
         {
            SetDeaths(cp, SetTo, 0, " `UniqueSkill");
            f.SquareShape(cp, 1, "50 + 1n Tank", 50, 0);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 50);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]); 
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         if (f.loop[cp] == 2)
         {
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         }
         if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.SquareShape(cp, 1, "50 + 1n Tank", 50, 50);
            f.SquareShape(cp, 1, "50 + 1n Tank", 50, 0);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 50);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]); 
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.SquareShape(cp, 1, "50 + 1n Tank", 50, 0);
            f.SquareShape(cp, 1, "50 + 1n Tank", 50, 50);
            f.SquareShape(cp, 1, "50 + 1n Tank", 100, 0);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 50);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]); 
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         if (f.loop[cp] == 8)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.SquareShape(cp, 1, "50 + 1n Tank", 50, 0);
            f.SquareShape(cp, 1, "50 + 1n Tank", 50, 50);
            f.SquareShape(cp, 1, "50 + 1n Tank", 100, 0);
            f.SquareShape(cp, 1, "50 + 1n Tank", 100, 100);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 50);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]); 
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 10)
         {
         f.count[cp] += 1;
         f.loop[cp] = 0;
         }

      }
         
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         }
         if (f.loop[cp] == 8 )
         {
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 0, 150);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);     
         }

       f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 12)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.SkillEnd(cp);
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
   }
}
