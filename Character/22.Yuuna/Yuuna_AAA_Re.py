import Function as f;

const s = StringBuffer();
function FlowerShape(cp : TrgPlayer, count, Unit : TrgUnit, i, distance, interval);

function main(cp)
{
   MoveLocation("22.Yuuna_Bozo", f.heroID[cp], cp, "Anywhere");
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);
   
   f.BanReturn(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {         
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");
            SetSwitch("Recall - Yuuna", Set);

            f.SkillWait(cp, 2080);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.Voice_Routine(cp, 9);
            f.SkillWait(cp, 5760);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopB[cp] = 0;
         }

      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {         
            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 3, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 3, 75);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 480);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 4, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 4, 75);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 480);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 5, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 5, 75);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 800);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 7, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 7, 75);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 480);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 9, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 9, 75);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 480);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 11, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 11, 75);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 9040);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 17)
         {         
            KillUnitAt(11, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 17)
         {         
            f.SkillWait(cp, 400);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] == 0)
         {         
            f.Voice_Routine(cp, 10);
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 11, 100 + 50 * f.loop[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 3)
         {         
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 11, 100 + 50 * f.loop[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            f.EdgeShape(cp, 1, "50 + 1n Tank", 0, 11, 100 + 50 * f.loop[cp]);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 5, 100 + 50 * 0);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 7, 100 + 50 * 1);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 9, 100 + 50 * 2);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            f.EdgeShape(cp, 1, "60 + 1n Siege", 0, 11, 100 + 50 * 3);

            f.SkillWait(cp, 1200);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopB[cp] = 0;
         }

      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] == 0)
         {         
            f.Voice_Routine(cp, 11);

            f.SkillWait(cp, 4240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 3)
         {         
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 9, 75);
            f.NxNSquareShape(cp, 1, "40 + 1n Goliath", 9, 75);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, "Anywhere");
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopB[cp] = 0;
         }
      }
      else if (f.count[cp] == 5)
      {
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         SetSwitch("Recall - Yuuna", Clear);
         SetSwitch("UiltimateSwitch", Clear);
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
         f.SkillEnd(cp);
      }
   }

   if (f.delayB[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loopB[cp] < 4)
         {
            var x = 50 * f.loopB[cp];
            var y = 200 - 50 * f.loopB[cp];

            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] < 7)
         {
            var x = 200 - 50 * (f.loopB[cp] - 4);
            var y = -50 * (f.loopB[cp] - 4);

            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] == 7)
         {
            var x = 200 - 50 * (f.loopB[cp] - 4);
            var y = -50 * (f.loopB[cp] - 4);

            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loopB[cp] < 4)
         {
            var x = 50 * f.loopB[cp];
            var y = 200 - 50 * f.loopB[cp];

            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", y, -x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] < 7)
         {
            var x = 200 - 50 * (f.loopB[cp] - 4);
            var y = -50 * (f.loopB[cp] - 4);

            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", y, -x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] == 7)
         {
            var x = 200 - 50 * (f.loopB[cp] - 4);
            var y = -50 * (f.loopB[cp] - 4);

            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", y, -x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] = 0;
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loopB[cp] < 7)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.LineShape(cp, 1, "50 + 1n Tank", 45 * 3 * f.loopB[cp] + 90, 11, 75, 100);
            f.LineShape(cp, 1, "40 + 1n Guardian", 45 * 3 * f.loopB[cp] + 180, 11, 75, 100);
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 45 * 3 * f.loopB[cp], 11, 75, 100);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] == 7)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.LineShape(cp, 1, "50 + 1n Tank", 45 * 3 * f.loopB[cp] + 90, 11, 75, 100);
            f.LineShape(cp, 1, "40 + 1n Guardian", 45 * 3 * f.loopB[cp] + 180, 11, 75, 100);
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 45 * 3 * f.loopB[cp], 11, 75, 100);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] = 0;
         }
      }
   }
}
