import Function as f;

function main(cp)
{
   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

         var d = 105 - 10 * f.loop[cp];

         f.EdgeShape(cp, 1, "40 + 1n Mutalisk", 45, 3, d);
         f.EdgeShape(cp, 1, "Protoss Dark Archon", 45, 3, d);
         KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);

         f.EdgeShape(cp, 1, "Bengalaas (Jungle)", 45, 3, 50);
         f.DotShape(cp, 1, "40 + 1n Guardian", 0, 0);
         KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
         }

         if (f.loop[cp] < 2)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 45, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else if (f.loop[cp] < 6)
         {
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            var i = f.loop[cp] - 2;

            var x = 50 - 50 * i;
            var y = 100;

            f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y);
            f.SquareShape(cp, 1, "Rhynadon (Badlands)", x, y);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);

            x = 100 - 50 * i;
            y = 100;

            f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y);
            f.SquareShape(cp, 1, "Bengalaas (Jungle)", x, y);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);

            if (f.loop[cp] == 5)
            {
               f.SquareShape(cp, 1, "Target", 150, 150);
               KillUnitAt(All, "Target", "Anywhere", cp);
            }
         }
         else if (f.loop[cp] == 6)
         {
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.SquareShape(cp, 1, "Target", 50, 50);
            KillUnitAt(All, "Target", "Anywhere", cp);
         }
         else if (f.loop[cp] == 7)
         {
            f.DotShape(cp, 1, "Target", 0, 0);
            KillUnitAt(All, "Target", "Anywhere", cp);
         }
         else if (f.loop[cp] == 8)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Mutalisk", 3, 50);
            f.NxNSquareShape(cp, 1, "Rhynadon (Badlands)", 3, 50);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 10)
         {
            f.EdgeShape(cp, 1, "Rhynadon (Badlands)", 45, 5, 100);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 12)
         {
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

         f.Table_Sin(cp, 30 * f.loop[cp], 100);
         f.Table_Cos(cp, 30 * f.loop[cp], 100);

         f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);
         f.SquareShape(cp, 1, "40 + 1n Goliath", f.CosAngle[cp], f.SinAngle[cp]);

         KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
         Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}