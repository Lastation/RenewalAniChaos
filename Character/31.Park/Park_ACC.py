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
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");
            f.SquareShape(cp, 1, "40 + 1n Guardian", 75, 25);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 25, 75);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 75, 25);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 25, 75);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]); 
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         if (f.loop[cp] == 2)
         {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
         }
         if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Guardian", 75, 0);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 50, 50);
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]); 
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 75, 0);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 50, 50);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         if (f.loop[cp] == 8)
         {
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 75, 0);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 50, 50);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 100);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 125, 0);
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]); 
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
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
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         f.DoubleShape(cp, 1, "40 + 1n Guardian", 125, 0);
         f.SquareShape(cp, 1, "40 + 1n Mutalisk", 75, 0);
         f.SquareShape(cp, 1, "40 + 1n Mutalisk", 75, 75);
         f.SquareShape(cp, 1, "Protoss Dark Archon", 75, 0);
         f.SquareShape(cp, 1, "Protoss Dark Archon", 0, 75);
         KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
         Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);      
         }
         if (f.loop[cp] == 3 )
         {
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            f.DoubleShape(cp, 1, "40 + 1n Guardian", 0, 125);
            f.NxNSquareShape(cp, 1, "40 + 1n Mutalisk", 3, 75);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 3, 75);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);  
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);   
         }
         if (f.loop[cp] == 6 )
         {
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            f.DoubleShape(cp, 1, "40 + 1n Guardian", 125, 0);
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 75, 0);
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 75, 75);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 75, 0);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 0, 75);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]); 
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);    
         }
         if (f.loop[cp] == 9 )
         {
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            f.DoubleShape(cp, 1, "40 + 1n Guardian", 0, 125);
            f.NxNSquareShape(cp, 1, "40 + 1n Mutalisk", 3, 75);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 3, 75);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);  
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);   
         }
       f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 12)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         }
         if (f.loop[cp] == 6 )
         {
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            f.EdgeShape(cp, 1, "40 + 1n Goliath", 45,3, 32);
            f.EdgeShape(cp, 1, "50 + 1n Tank", 45,3, 32);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);     
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);     
         }
         if (f.loop[cp] == 10 )
         {
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            f.EdgeShape(cp, 1, "40 + 1n Goliath", 45,3, 32);
            f.EdgeShape(cp, 1, "50 + 1n Tank", 45,3, 32);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);     
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);     
         }

       f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 12)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
            f.SkillEnd(cp);
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
   }
}
