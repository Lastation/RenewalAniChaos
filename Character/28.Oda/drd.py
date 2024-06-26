import Function as f;

function main(cp)
{
   MoveUnit(All, "40 + 1n Goliath", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "50 + 1n Tank", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "40 + 1n Marine", cp, "Anywhere", "[Skill]HoldPosition");

   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 4)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            var x = 50 - 50 * f.loop[cp];
            var y = 100;

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
            f.SquareShape(cp, 1, "50 + 1n Tank", x, y);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }



         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         var i = f.loop[cp];

         if (f.loop[cp] == 0)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }

         if (f.loop[cp] < 3)
         {
            f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 3 + 2 * i, 50 + 50 * i);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         }
         else if (f.loop[cp] < 7)
         {
            f.EdgeShape(cp, 1, "40 + 1n Wraith", 45, 7 - 2 * (i - 3), 150 - 50 * (i - 3));
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         }

         if (f.loop[cp] == 2)
         {
            f.SquareShape(cp, 1, "60 + 1n Siege", 150, 150);
            f.SquareShape(cp, 1, "60 + 1n Siege", 75, 150);
            f.SquareShape(cp, 1, "60 + 1n Siege", 150, 75);
         }
         else if (f.loop[cp] == 4)
         {
            RemoveUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 19)
         {
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         var i = f.loop[cp];

         if (f.loop[cp] == 0)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }

         if (f.loop[cp] < 3)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 3 + 2 * i, 50 + 50 * i);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else if (f.loop[cp] < 11)
         {
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 5, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SquareShape(cp, 1, "60 + 1n High Templar", 120 - 15 * (i - 3), 15 * (i - 3));
            f.SquareShape(cp, 1, "60 + 1n High Templar", 10 * (i - 3), 80 - 10 * (i - 3));   
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
         }

         if (f.loop[cp] == 3)
         {
            f.EdgeShape(cp, 1, "40 + 1n Marine", 0, 5, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 11)
         {
            KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Wraith", 0, 5, 100);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 17)
         {
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         f.SkillEnd(cp);
      }
   }
}